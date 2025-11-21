def fib(n):
    """计算第 n 个斐波那契数（n ≥ 1）"""
    if not isinstance(n, int) or n < 1:
        raise ValueError("n 必须是大于等于 1 的整数")
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    # 本地运行测试
    print(fib(5))  # 输出：5
    print(fib(10)) # 输出：55