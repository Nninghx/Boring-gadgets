# 导入所需的库  
from tqdm import tqdm  # 显示进度条
import decimal  # 高精度计算
import os  # 文件和目录操作
import pickle  # 对象的序列化和反序列化


# 定义一个函数，记忆圆周率计算点，避免程序以外中断导致数据丢失
def load_checkpoint(checkpoint_file):
    """  
    加载文件，如果存在，则返回保存的数据；否则返回None。
    """
    if os.path.exists(checkpoint_file):  # 判断文件是否存在  
        with open(checkpoint_file, 'rb') as f:  # 以二进制读模式打开文件  
            return pickle.load(f)  # 使用pickle库加载数据  
    return None, None  # 如果文件不存在，则返回两个None  


# 定义一个函数，用于将当前状态保存到检查点文件
def save_checkpoint(checkpoint_file, k, pi_estimate):
    """  
    将当前的计算状态（k值和圆周率的估计值）保存到指定的检查点文件。  
    """
    with open(checkpoint_file, 'wb') as f:  # 以二进制写模式打开文件  
        pickle.dump((k, pi_estimate), f)  # 使用pickle库保存数据  


# 定义一个函数，用于计算圆周率到指定的小数位数
def pi_to_n_decimal_places(n, checkpoint_file='checkpoint.pkl'):
    """  
    使用指定的算法计算圆周率到n位小数，并支持从检查点恢复计算。  
    """
    decimal.getcontext().prec = n + 1  # 设置decimal库的计算精度  

    # 尝试从检查点文件加载数据  
    k, pi_estimate = load_checkpoint(checkpoint_file)
    if k is None:  # 如果没有检查点数据，则初始化变量  
        pi_estimate = decimal.Decimal(0)
        k = 0
    else:
        print(f"从检查点恢复计算，当前k值为 {k}")

        # 使用tqdm库显示进度条
    with tqdm(total=n + 1, desc="正在计算圆周率", leave=True, initial=k) as progress:
        while True:
            # 根据公式计算当前项的值  
            term = 1 / decimal.Decimal(16) ** k * (
                    decimal.Decimal(4) / (8 * k + 1) -
                    decimal.Decimal(2) / (8 * k + 4) -
                    decimal.Decimal(1) / (8 * k + 5) -
                    decimal.Decimal(1) / (8 * k + 6))
            # 判断当前项是否足够小，如果是则退出循环  
            if abs(term) < decimal.Decimal("1e-{}".format(n)):
                break
            pi_estimate += term  # 更新圆周率的估计值  
            k += 1  # 更新k值  
            progress.update(1)  # 更新进度条  

            # 保存当前状态到检查点文件  
            save_checkpoint(checkpoint_file, k, pi_estimate)

    return pi_estimate  # 返回计算得到的圆周率值  


# 主程序入口
if __name__ == '__main__':
    n = 2000000  # 设置要计算的圆周率的小数位数
    checkpoint_file = 'pi_checkpoint.pkl'  # 设置检查点文件的名称(文件名可以自定义)

    # 使用定义的函数计算圆周率  
    result = pi_to_n_decimal_places(n, checkpoint_file)

    # 将计算结果保存到文件中  
    with open('圆周率.txt', 'w') as f:
        f.write(str(result) + '\n')  # 将结果转换为字符串并写入文件