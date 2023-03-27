% 定义波束宽度（弧度）
bw = 0.1;
% 定义方位角（弧度）
az = pi/4;
% 定义俯仰角（弧度）
el = pi/6;
% 定义圆锥高度
h = 10;
% 计算圆锥半径
r = h * tan(bw/2);
% 计算圆锥底面中心坐标
cx = h * cos(az) * cos(el);
cy = h * sin(az) * cos(el);
cz = h * sin(el);
% 计算圆锥底面上的点坐标
theta = linspace(0, 2*pi, 100);
x = cx + r * cos(theta) * cos(az) - r * sin(theta) * sin(az) * cos(el);
y = cy + r * cos(theta) * sin(az) + r * sin(theta) * cos(az) * cos(el);
z = cz + r * sin(theta) * sin(el);
% 转换成极坐标
rho = sqrt(x.^2 + y.^2); % 半径
phi = atan2(y, x); % 角度
% 绘制极坐标图
figure
polar(phi, rho, 'b')
title('波束图')