Needs math, matplotlib and numpy libraries installed.
For windows to install the libraries open powershell and run: 
$> pip install <library>
Where library is the respective library you want to install

Use:

SHMOscillation class has five arguments:
  -num is the ID of the oscilation. You can insert any intiger.
  -name is the name of your oscilation so you can refer to it later on plotting. It can be a String
  -amplitude is the max and min values that your Oscillation can take. It can either be a Float or an Intiger
  -initialPhase is the starting point of your Oscillation. Again it can be an Integer or a Float
  -omega is the angular velocity of the Oscillation. It also can be an Integer or a Float
  
 Functions of SHMOscillation:
  -calculate takes an argument and that is time. You plug in the time and it prints the velocity and position
              of the Oscillation at that given time.
  -getValues returns an array with the initial values of the oscillation
  -printInfo Prints the initial values of the oscillation in a nice format
  -plotting Creates the plot objects of the Oscilation
  -showPlots Opens the figures of the previously created plot objects
  
Finaly to create an Oscilation you create a new object like this:

NameOfOscillation = SHMOscillation(num, name, amplitude, initialPhase, omega)
