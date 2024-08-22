import pandas as pd
import matplotlib.pyplot as plt

quit = False

original_df = pd.read_csv('Deaths_in_Australia.csv')

deaths_df = original_df.Show(rows=['Australia'])
deaths_df.head()

<<<<<<< HEAD
#deaths_df = pd.read_csv('Deaths_in_Australia.csv'
  #                      )
=======
deaths_df = pd.read_csv('Deaths_in_Australia.csv'
                             header=None
                             names=['Australia', 'Date', 'COD'])
>>>>>>> 5b3cda397f2b8d701f7cd232dcd30532d1540f33
                            

def showOriginalData():
    print(original_df)

def showUpdatedData(): 
    print(deaths_df)

def showCharts():
    deaths_df.plot(
                    kind='bar',
                    x='Date',
                    y='COD',
                    color='blue',
                    alpha=0.3,
                    title='Annual Deaths and Causes in Australia')
    plt.show()

def userOptions():
    global quit

    print("""Welcome to the Death Data Gathering!
          
          Please select an option:
          1 - Show the original dataset
          2 - Show the updated data frame
          3 - Show the graph for the amount of death with causes per year in Australia
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