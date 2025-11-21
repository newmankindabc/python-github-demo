import pytest
from fib import fib

def test_fib_positive():
    """测试正常输入"""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(5) == 5
    assert fib(10) == 55
    print("ok")

def test_fib_invalid():
    """测试非法输入（抛出异常）"""
    with pytest.raises(ValueError):
        fib(0)  # 小于 1
    with pytest.raises(ValueError):
        fib(-3) # 负数
    with pytest.raises(ValueError):
        fib(3.5) # 非整数