import sys


def get_inverse(value, p):
    """
    逆元を求め
    :param value: 逆元の值
    :param p: mod
    """
    for i in range(1, p):
        if (i * value) % p == 1:
            return i
            
    print('逆元が存在しない、無限遠点となります')

def get_gcd(value1, value2):
    """
    ユークリッド互除法
    :param value1:
    :param value2:
    """
    if value2 == 0:
        return value1
    else:
        return get_gcd(value2, value1 % value2)

def get_PaddQ(x1, y1, x2, y2, a, p):
    """
    P+Qを計算する
    :param x1: P点の横座標
    :param y1: P点の縦座標
    :param x2: Q点の横座標
    :param y2: Q点の縦座標
    :param a: 曲線のaの値
    :param p: 法P
    """
    flag = 1 # 

    # もしP=Qの場合，k=(3x^2+a)/2y mod p
    if x1 == x2 and y1 == y2:
        member = 3 * (x1 ** 2) + a # 分子
        denominator = 2 * y1 # 分母

    # もしP≠Qの場合， k=(y2-y1)/(x2-x1) mod p
    else:
        member = y2 - y1
        denominator = x2 - x1

        if member * denominator < 0:
            flag = 0 # 表示负数
            member = abs(member)
            denominator = abs(denominator)

    # 
    gcd = get_gcd(member, denominator) # 最大公約数
    member = member // gcd
    denominator = denominator // gcd
    # 分母の逆元
    inverse_deno = get_inverse(denominator, p)
    
    if inverse_deno == None:
        print('点の位数は1')
        sys.exit()
        
    # kを求める
    k = (member * inverse_deno)
    
    
    if flag == 0:
        k = -k
    k = k % p

    # P+Q=(x3,y3)を計算する
    x3 = (k ** 2 - x1 - x2) % p
    y3 = (k * (x1-x3) -y1) % p

    return x3, y3

def get_order(x0, y0, a, b, p):
    """0
    楕円曲線の位数と点の位数が違います。
    そこでしたら、点の位数です。
    何回繰り返したら、無限点になるのことです。
    """
    x1 = x0 # -P的横座標
    y1 = (-1 * y0) % p # -P的縦座標
    print(x0,y0)
    temp_x = x0
    temp_y = y0
    n = 0
    while True:
        n += 1
        # n*P=0∞計算する
        xp, yp = get_PaddQ(temp_x, temp_y, x0, y0, a, p)
        print(xp,yp)#スカラー倍の巡回
        # (xp,yp)==-Pの時，(xp,yp)+P=0∞，その時n+1は位数となる
        if xp == x1 and yp == y1:
            return n+1,print('点の位数は',n+1)#点の位数
            
        temp_x = xp
        temp_y = yp
        
def get_dot(x0, a, b, p):
    """
    Pと-Pを計算する
    """
    y0 = -1
    for i in range(p):
        # 楕円曲線の条件、Ep(a,b)，pは素数，x,y∈[0,p-1]
        if i**2 % p == (x0**3 + a*x0 + b) % p:
            y0 = i
            break
    # 
    if y0 == -1:
        return False
    # -y
    x1 = x0
    y1 = (-1*y0) % p
    #print(x1,y1)
    return x0, y0, x1, y1
'''

'''
def get_nG(xG, yG, priv_key, a, p):
    """
    
    """
    temp_x = xG
    temp_y = yG
    while priv_key != 1:
        temp_x, temp_y = get_PaddQ(temp_x, temp_y, xG, yG, a, p)
        priv_key -= 1
    return temp_x, temp_y

def get_KEY():
    """
    
    """
    # 方程式を決める
    while True:
        a = int(input('a（a>0）の值を入力してください：'))
        b = int(input('b（b>0）の值を入力してください：'))
        p = int(input('楕円曲線の素数ｐを入力してください：'))

        # 判別式
        if (4*(a**3)+27*(b**2))%p == 0:
            print('エラー、もう一度確認してください\n')
        else:
            break
    # 
    print('基準点を決めてください')
    xG = int(input('横座標xG：'))
    yG = int(input('縦座標yG：'))

    # 
    n = get_order(xG, yG, a, b, p)

    # 
    priv_key = int(input('秘密鍵key：'))
    #
    xK, yK = get_nG(xG, yG, priv_key, a, p)
    return xK, yK, priv_key, a, b, p, n, xG, yG

def encrypt(xG, yG,priv_key, a, p, n):
    """
    暗号化
    """
    kGx, kGy = get_nG(xG, yG, priv_key, a, p) # kG
    print(kGx,kGy)
    return kGx,kGy



if __name__ == '__main__':
    
    #c = encrypt(xG, yG,priv_key, a, p, n)
    #c1 = encrypt(4,1,10,0,11,11)
    #print(c1)
    #print('テスト')
    m=get_order(7,0,1,2,11)
    #c=get_order(2,0,0,3,11)
