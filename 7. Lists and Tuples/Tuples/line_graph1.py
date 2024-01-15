#programme to print a simpel grah

import matplotlib.pyplot as plt


def main():
    x_coords=[0,1,2,3,4]
    y_coords=[0,3,1,5,2]

    #lets build a graph

    plt.plot(x_coords,y_coords)

#add a title
    plt.title('Sample data')

    #add labels
    plt.xlabel('This is the X axis')
    plt.ylabel('This is the Y axis')


    
    #display
    plt.show()

#call main function
if __name__ == '__main__':
    main()