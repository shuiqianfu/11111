import bisect


def main():
    n = int(input().strip())
    M = []  # 使用有序列表存储集合元素
    output_lines = []  # 存储输出结果

    for _ in range(n):
        data = input().split()
        opt = int(data[0])

        if opt == 1:  # 插入操作
            x = int(data[1])
            pos = bisect.bisect_left(M, x)
            # 如果元素不存在，则插入到正确位置
            if pos == len(M) or M[pos] != x:
                M.insert(pos, x)

        elif opt == 2:  # 删除操作
            x = int(data[1])
            pos = bisect.bisect_left(M, x)
            # 如果元素存在，则删除
            if pos < len(M) and M[pos] == x:
                del M[pos]

        elif opt == 3:  # 存在性查询
            x = int(data[1])
            pos = bisect.bisect_left(M, x)
            # 检查元素是否存在
            if pos < len(M) and M[pos] == x:
                output_lines.append("YES")
            else:
                output_lines.append("NO")

        elif opt == 4:  # 大小查询
            output_lines.append(str(len(M)))

        elif opt == 5:  # 前驱查询
            x = int(data[1])
            pos = bisect.bisect_left(M, x)
            # 前驱是小于x的最大元素
            if pos > 0:
                output_lines.append(str(M[pos - 1]))
            else:
                output_lines.append("-1")

        elif opt == 6:  # 后继查询
            x = int(data[1])
            pos = bisect.bisect_right(M, x)
            # 后继是大于x的最小元素
            if pos < len(M):
                output_lines.append(str(M[pos]))
            else:
                output_lines.append("-1")

    # 输出所有结果
    for line in output_lines:
        print(line)


if __name__ == "__main__":
    main()111