<h1 align="center"> Influential Simplices Mining via Simplicial Convolutional Networks </h1>

<div align="center">
  <a href="http://yujie.world/">Yuejie Zeng</a> <sup>1</sup> &ensp; <b>&middot;</b> &ensp;
  <a href="https://yimingh.top/">Yiming Huang</a> <sup>2</sup> &ensp; <b>&middot;</b> &ensp;
  <a href="https://scholar.google.co.uk/citations?hl=en&user=edUqF7sAAAAJ&view_op=list_works&sortby=pubdate">Qiang Wu</a> <sup>3</sup> &ensp; <b>&middot;</b> &ensp;
  <a href="https://linyuanlab.com/">Linyuan Lü</a> <sup>4</sup>
  <br> <br> 
<sup>1</sup> yujie_zeng@std.uestc.edu.cn  
<sup>2</sup> y.huang24@imperial.ac.uk <br> 
<sup>3</sup> qiang.wu@uestc.edu.cn 
<sup>4</sup> linyuan.lv@ustc.edu.cn
</div>

<h3 align="center"> 
[<a href="https://www.sciencedirect.com/science/article/abs/pii/S0306457324001729?via%3Dihub">PDF</a>]
[<a href="https://arxiv.org/pdf/2307.05841">arXiv</a>]
[<a href="https://mp.weixin.qq.com/s/DnmGTCx0EJ873OsnW1_jYQ">公众号推文</a>]

</h3>


Official Implementations of ISMnet(*Information Processing & Management 2024)*.

![visitors](https://visitor-badge.laobi.icu/badge?page_id=Yiminghh/HiGCN)

Detected an inconsistency between mining influential nodes and simplices. Innovatively formulated the influential simplices mining task as a graph learning problem and designed an influential simplices mining neural network (ISMnet) that achieves SOTA performance in this task.
<div align="center">
    <img src="figs/framework.png" alt="Framework">
</div>



# Installation
This code is developed with Python3, and we recommend python>=3.8 and PyTorch ==1.13.0. Install the dependencies with Anaconda and activate the environment with:

    conda create --name GOUB python=3.8
    conda activate GOUB
    pip install -r requirements.txt



# Important Option Details
* `dataroot_GT`: Ground Truth (High-Quality) data path.
* `dataroot_LQ`: Low-Quality data path.
* `pretrain_model_G`: Pretraind model path.
* `GT_size, LQ_size`: Size of the data cropped during training.
* `niter`: Total training iterations.
* `val_freq`: Frequency of validation during training.
* `save_checkpoint_freq`: Frequency of saving checkpoint during training.
* `gpu_ids`: In multi-GPU training, GPU ids are separated by commas in multi-gpu training.
* `batch_size`: In multi-GPU training, must satisfy relation: *batch_size/num_gpu>1*.


# Citation
Please cite our work if you find our code/paper is useful to your work. :
```latex
@article{ISMnet2024, 
    title = {Influential simplices mining via simplicial convolutional networks}, 
    journal = {Information Processing \& Management}, 
    author = {Yujie Zeng and Yiming Huang and Qiang Wu and Linyuan L{\"u}}, 
    volume = {61}, 
    number = {5}, 
    pages = {103813}, 
    year = {2024}, 
    issn = {0306-4573}, 
    doi = {https://doi.org/10.1016/j.ipm.2024.103813}, 
    url = {https://www.sciencedirect.com/science/article/pii/S0306457324001729}, 
}
```


 
🍀 **Thank you for your interest in our work.** 🍀

If you have any questions or encounter any issues while using our code, please don't hesitate to raise an issue or reach out to us directly.

