print("testing1")
def main():
    outfile = open('philosophers.txt','w')
    outfile.write('John Locke\n')
    outfile.write('Zavid Hume\n')
    outfile.write('Edmund Burke\n')
    outfile.close()
    print("testing1")

if __name__ == '__main__':
    main()