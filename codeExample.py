import enotipy.enotipy as enotipy

if __name__ == "__main__":
    #The function to be executed
    def test_fcn(*args):
        x, = args;
        for i in range(x):
            print(i)

    # notipy.requestEnvSetup() #This option requests user input to set environment
    args = (10,)
    enotipy.infoFileEnvSetup("./INFO") #This option sets the environment with an info file
    # enotipy.infoFileEnvSetup("./SAMPLE_INFO") #This option sets the environment with an info file
    notifier = enotipy.ENotiPy() #Creating notipy object
    notifier.run(test_fcn,*args) #Calling run to execute the function and send email when completed.
