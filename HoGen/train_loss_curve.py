import os
import re
import numpy as np
import matplotlib.pyplot as plt
import pickle



def process_logs_and_plot():

    with open('./data/train_loss_curve.pkl', 'rb') as f:
        ho_losses, OU_losses, noise_losses = pickle.load(f)

    # 计算均值和标准差
    ho_mean, ho_std = np.nanmean(ho_losses, axis=0), np.nanstd(ho_losses, axis=0)
    OU_mean, OU_std = np.nanmean(OU_losses, axis=0), np.nanstd(OU_losses, axis=0)
    noise_mean, noise_std = np.nanmean(noise_losses, axis=0), np.nanstd(noise_losses, axis=0)

    # 计算 combined_mean 和 combined_std
    # 确保 ho_mean 和 OU_mean 长度一致
    max_length_combined = max(len(ho_mean), len(OU_mean))

    # Pad ho_mean and OU_mean to max_length_combined
    def pad_array(arr, target_length):
        if len(arr) < target_length:
            return np.pad(arr, (0, target_length - len(arr)), mode='constant', constant_values=np.nan)
        return arr

    ho_mean_padded = pad_array(ho_mean, max_length_combined)
    OU_mean_padded = pad_array(OU_mean, max_length_combined)
    combined_mean = ho_mean_padded + OU_mean_padded

    # Compute combined_std assuming independence
    ho_std_padded = pad_array(ho_std, max_length_combined)
    OU_std_padded = pad_array(OU_std, max_length_combined)
    combined_std = np.sqrt(np.square(ho_std_padded) + np.square(OU_std_padded))

    # 计算 noise_mean 和 noise_std 对应的 max_length_total
    max_length_total = max(max_length_combined, len(noise_mean))
    combined_mean = pad_array(combined_mean, max_length_total)
    combined_std = pad_array(combined_std, max_length_total)
    noise_mean = pad_array(noise_mean, max_length_total)
    noise_std = pad_array(noise_std, max_length_total)

    # 也需要 pad ho_mean, OU_mean 和 ho_std, OU_std
    ho_mean_padded = pad_array(ho_mean, max_length_total)
    ho_std_padded = pad_array(ho_std, max_length_total)
    OU_mean_padded = pad_array(OU_mean, max_length_total)
    OU_std_padded = pad_array(OU_std, max_length_total)

    # 绘制平均曲线和阴影范围
    plt.figure(figsize=(9, 8))
    steps = np.arange(max_length_total)

    # 绘制 Noise losses
    line_classical, = plt.plot(steps, noise_mean, label="Classical", color="#b5d1e2",alpha=0.9)
    plt.fill_between(steps, noise_mean - noise_std, noise_mean + noise_std, color="#b5d1e2", alpha=0.36, edgecolor="none")

    # 绘制 HO losses
    line_ho, =plt.plot(steps, ho_mean_padded, label="Coarse", color="#e99462")
    plt.fill_between(steps, ho_mean_padded - ho_std_padded, ho_mean_padded + ho_std_padded, color="#e99462", alpha=0.26, edgecolor="none")

    # 绘制 OU losses
    line_OU, =plt.plot(steps, OU_mean_padded, label="Fine", color="#944990",alpha=0.78)
    plt.fill_between(steps, OU_mean_padded - OU_std_padded, OU_mean_padded + OU_std_padded, color="#944990", alpha=0.26, edgecolor="none")

    # 绘制 Combined losses
    line_comb,=plt.plot(steps, combined_mean, label="Coarse+Fine", color="#c82423",alpha=0.9)
    plt.fill_between(steps, combined_mean - combined_std, combined_mean + combined_std, color="#c82423", alpha=0.2, edgecolor="none")

    from matplotlib.legend_handler import HandlerLine2D
    # 设置图形信息
    xticks = np.arange(0,20000+1,3000)
    xticks_labels = [f"{x / 10000:.1f}" for x in xticks]  # 转换为缩放后的刻度标签
    xticks_labels[0]='0'
    plt.xticks(xticks, xticks_labels)  # 设置新的刻度标签
    plt.tick_params(axis='both', labelsize=29)  # 'both' 表示同时调整 x 和 y 轴
    plt.xlabel("Training Steps ($\\times 10^4$)", fontsize=29)
    plt.ylabel("Spectrum Loss", fontsize=29)
    plt.xlim(-500, 20000)  # 根据需要调整
    plt.ylim(0, 7.6)  # 根据需要调整

    legend = plt.legend(fontsize=29,frameon=False,
                        handles=[line_ho,line_OU,line_comb,line_classical],
                        labels=['Coarse','Fine','Coarse+Fine','Classical (Noise)'])  # 添加图例
    for legend_line in legend.get_lines():
        legend_line.set_linewidth(8)  # 调整图例中线条的宽度为
    plt.grid(True)

    # 保存图片为 PDF 格式
    plt.savefig("../fig/training_loss.svg", format="svg", bbox_inches="tight")  # bbox_inches="tight" 确保内容不被裁剪
    plt.show()


if __name__ == '__main__':
    process_logs_and_plot()
