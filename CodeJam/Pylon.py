import sys
if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    T = int(f.readline())
    for _T in xrange(T):
        R, C = map(int, f.readline().split())
        _R, _C = R, C

        reverse = False
        if R < C:
            reverse = True
            R, C = C, R

        c_offset = 0

        squares = []
        def emit(i, j):
            j += c_offset
            if reverse:
                squares.append((j, i))
            else:
                squares.append((i, j))

        while R >= 5 and C >= 4:
            y = 1
            emit(y, 1)
            while True:
                emit(y+3, 2)
                emit(y+1, 1)
                y += 1
                if y == R - 2:
                    break
            emit(1, 2)
            emit(R - 1, 1)
            emit(2, 2)
            emit(R, 1)
            emit(3, 2)

            C -= 2
            c_offset += 2

        hit = {}
        for x in xrange(1, R+1):
            for y in xrange(1, C+1):
                hit[(x, y)] = False

        def search(x, y):
            hit[(x, y)] = True
            emit(x, y)

            if all(hit.values()):
                raise IOError()

            for i in xrange(1, R+1):
                for j in xrange(1, C+1):
                    if hit[(i, j)]:
                        continue
                    if i == x:
                        continue
                    if j == y:
                        continue
                    if i + j == x + y:
                        continue
                    if i - j == x - y:
                        continue

                    search(i, j)
            hit[(x, y)] = False
            squares.pop()

        try:
            search(2, 2)
        except IOError:
            assert len(squares) == _R * _C, len(squares)
            assert len(set(squares)) == len(squares)
            for r, c in squares:
                assert 1 <= r <= _R, (r, c)
                assert 1 <= c <= _C, (r, c)
            for i in xrange(len(squares) - 1):
                r, c = squares[i]
                x, y = squares[i + 1]
                assert r != x
                assert c != y
                assert r + c != x + y
                assert r - c != x - y

            print "Case #%d: POSSIBLE" % (_T + 1,)
            for x, y in squares:
                print x, y
        else:
            print "Case #%d: IMPOSSIBLE" % (_T + 1,)

