from src.pass_gen import password_generator


if __name__=='__main__':
    min_length=int(input("Enter the minimum length: "))
    number=input("Do you want to have number(y/n)?: ").lower() == 'y'
    special_charcater=input("Do you want to special charcater(y/n)?: ").lower() == 'y'


    my_pass=password_generator(min_length=min_length,number=number,special_charcater=special_charcater)
    print(my_pass)