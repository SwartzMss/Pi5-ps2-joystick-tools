# Pi5-ps2-joystick-tools

这是一个示例仓库，展示如何在树莓派 Pi5 上通过 ADS1115 模数转换器读取 PS2 摇杆模块的数值。

## 连接方式

1. 将摇杆的 `VRx` 尖脚连接到 ADS1115 的 `A0`（`P0`）。
2. 将摇杆的 `VRy` 尖脚连接到 ADS1115 的 `A1`（`P1`）。
3. *(可选)* 将摇杆的按键尖脚连接到树莓派的某个 GPIO（示例中为 GPIO17）。如果只需要 X/Y 两个模拟量，可不接此线，并在代码中禁用按键读取。
4. 其余电源和 GND 尖脚按常规方式接线。

如果没有连接按键线，在创建 `Joystick` 实例时将 `button_pin` 参数设为 `None`：

```python
from joystick import Joystick

joy = Joystick(button_pin=None)
```

## 运行示例

仓库中提供了两个 Python 脚本，分别依赖 `gpiozero` 和 `adafruit-circuitpython-ads1x15`。安装依赖后你可以以以下方式运行：

```bash
pip install gpiozero adafruit-blinka adafruit-circuitpython-ads1x15
python examples/main.py
```

`examples/main.py` 使用 `examples/joystick.py`中的 `Joystick` 类来读取摇杆数据，并周期输出 X/、Y 值及按键状态。按 `Ctrl+C` 可退出。
