clear all;close all;clc



correlation = [1.0, 0.899, 0.819, 0.488, 0.265;
        0.899, 1.0, 0.833, 0.135, 0.127;
        0.819, 0.833, 1.0, 0.218, -0.022;
        0.488, 0.135, 0.218, 1.0, 0.499;
        0.265, 0.127, -0.022, 0.449, 1.0];

%%
%correlation=corr_Grid;
xyname = {'a','b','c','d','e'};
h=heatmap(xyname,xyname,correlation,'CellLabelFormat','%0.3f',...
    'Colormap',summer,'GridVisible','off');
% 'CellLabelColor','w'
set(gca,'FontSize',23);
set(gcf,'Units','centimeters','Position',[1 1 17 15]);
%
mycolorpoint=[242 250 235;...
    211 238 205;...
    165 219 183;...
    101 192 203;...
    47 143 191;...
    8 91 160;...
    8 68 133];

num_mycolorpoint=length(mycolorpoint);
mycolorposition=[1 13 23 33 46 55 64];%采样点
mycolormap_r=interp1(mycolorposition,mycolorpoint(:,1),1:64,'linear','extrap');
mycolormap_g=interp1(mycolorposition,mycolorpoint(:,2),1:64,'linear','extrap');
mycolormap_b=interp1(mycolorposition,mycolorpoint(:,3),1:64,'linear','extrap');
mycolor=[mycolormap_r',mycolormap_g',mycolormap_b']/255;
mycolor=round(mycolor*10^4)/10^4;%保留4位小数
colormap(mycolor)

