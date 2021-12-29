#SANNUNANDU74EC

def convertYNtoBoolean(li):
    for i in range(len(li)):
        if(li[i] == 'y' or li[i]=='Y'):
            li[i] = True
        elif(li[i] == 'n' or li[i]=='N'):
            li[i] = False
        else:
            li[i] = False
    return li
    # end
    
def intro():
    return '''
    INSTRUCTIONS :
    ------------
    The input option will be shown.
    give Y/y for yes
    give N/n for no
    for inputs.
    '''
    # end
    
def displayInformation():
    return '''
        INFORMATION :
        ------------
        *PCR : Polymerase chain reaction, Detect genetic material from a specific organisim like virus. This can be a nasal swab or a bit of saliva.
        * Serious Symptoms :
            * Difficult breathing or shortness of breath
            * Loss of speech or mobility, or confusion
            * chest pain
        * Most common symptoms :
            * fever
            * Cough
            * Tiredness
            * Loss of taste or smell
     '''
     # end
    
 def seriousSymptomsInput():
     result = [False,False,False]
     print("--------------------------------------------------------")
     result[0] = input( " [1] Difficult breathing or shortness of breath : " )
     result[1] = input( " [2] Loss of speech or mobility, or confusion   : " )
     result[2] = input( " [3] chest pain                                 : " )
     result = convertYNtoBoolean(result)
     return result
     # end
    
 def mostCommonSymptomsInput():
     result = [False,False,False,False]
     print("----------------------------------------------------------")
     result[0] = input( " [1] fever                    : " )
     result[1] = input( " [2] cough                    : " )
     result[2] = input( " [3] Tiredness                : " )
     result[3] = input( " [4] Loss of taste or smell   : " )
     result = convertYNtoBoolean(result)
     return result
     # end
      
 # main code
 print(displayInformation())
 print(intro())

 symptom1 = seriousSymtomsInput()
 symptom2 = mostCommonSymptomsInput()

 symptomaticResult = "negative"
 # checking symptom1
 # If one synptom occur then there is high possibility of covid 19
 if symptom1[0] or symptom1[1] or symptom1[2] :
     symptomaticResult = "positive"
 elif symptom2[0] and symptoms2[1] and symptom2[1] and symptoms2[2] and symptom2[3]:
    symptomaticResult = "positive"
    
    
 print("-----------------------------------------------------------------")
 asymptomatic = input(" [1] PCR test result : ")
  
 if asymptomatic == 'y' or asymptomatic == 'Y' :
     print(" ( Asymptomatic) Covid positive")
 else:
     print(" ( Asymptomatic) Covid negative")
    
 print(" ( Symptomatic) Covid" + symtomaticResult)
    
    
    
    
    
    
    
    
 
 
                                 
    
    
    
    
    
    
    
    
           
    
