#programme to print a simpel grah

import matplotlib.pyplot as plt


def main():
    x_coords=[0,1,2,3,4]
    y_coords=[0,3,1,5,2]

    #lets build a graph

    plt.plot(x_coords,y_coords)

    #display
    plt.show()

#call main function
if __name__ == '__main__':
    main()