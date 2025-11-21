def fib(n):
    # 原有代码不变...

def fib_batch(count):
    """批量生成前 count 个斐波那契数（count ≥ 1）"""
    if not isinstance(count, int) or count < 1:
        raise ValueError("count 必须是大于等于 1 的整数")
    return [fib(i) for i in range(1, count + 1)]

if __name__ == "__main__":
    print(fib_batch(5))  # 输出：[1, 1, 2, 3, 5]