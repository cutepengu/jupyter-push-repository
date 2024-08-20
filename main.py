import pandas as pd
import matplotlib.pyplot as plt

quit = False

original_df = pd.read_csv('Deaths_in_Australia.csv')


deaths_df = pd.read_csv('Deaths_in_Australia.csv')
                            

def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(deaths_df)

def showCharts():
    deaths_df.plot(
                    kind='bar',
                    x='Country',
                    y='Date',
                    color='blue',
                    alpha=0.3,
                    title='Annual Deaths in Australia')
    plt.show()

def userOptions():
    global quit

    print("""Welcome to the Death Data Gathering!
          
          Please select an option:
          1 - Show the original dataset
          2 - Show the updated data frame
          3 - Show the graph for the amount of death per year
          4 - Quit program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 4:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   
while not quit:
    userOptions()