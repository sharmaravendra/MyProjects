# def calculate_total(exp):
#     total=0
#     for item in exp:
#         total=total+item
#     return total
# tom_exp_list=[2100,3400,3500]
# joe_exp_list=[200,500,700]
# toms_total=calculate_total(tom_exp_list)
# joes_total=calculate_total(joe_exp_list)
# print("Tom's total:",toms_total)
# print("Joe's total:",joes_total)
# def sum(a,b):
#     total=a+b
#     return(total)
#
# total=sum(b=5,a=6)
# print(total)
def sum(a,b=0):
    """
    :param a:
    :param b:
    :return: 
    """
    total=a+b
    return total

total=sum(2,3)
print(total)
