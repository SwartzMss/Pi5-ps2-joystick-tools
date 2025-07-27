# Pi5-ps2-joystick-tools

这是一个示例仓库，展示如何在树莓派 Pi5 上通过 ADS1115 模数转换器读取 PS2 摇杆模块的数值。

## 连接方式

1. 将摇杆的 `VRx` 尖脚连接到 ADS1115 的 `A0`（`P0`）。
2. 将摇杆的 `VRy` 尖脚连接到 ADS1115 的 `A1`（`P1`）。
3. 其余电源和 GND 尖脚按常规方式接线。


## 运行示例

仓库中提供了两个 Python 脚本，依赖 `adafruit-circuitpython-ads1x15`。安装依赖后可以通过以下命令运行：

```bash
pip install adafruit-blinka adafruit-circuitpython-ads1x15 lgpio
python examples/main.py
```

`examples/main.py` 使用 `examples/joystick.py`中的 `Joystick` 类来读取摇杆数据，并周期输出 X、Y 值。按 `Ctrl+C` 可退出。
