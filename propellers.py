import torch


class Propellers():
    """
    Class of n propellers. Operates on torch.tensors and uses physics simulation of real-life propellers.
    Credits: https://www.electricrcaircraftguy.com/2013/09/propeller-static-dynamic-thrust-equation.html

    Attributes:
        n (int): Number of propellers, operating in one class.
        dia (torch.tensor): Vector of shape (n), containing torch.float values of diameters (meter).
        pitch (torch.tensor): Vector of shape (n), containing torch.float values of pitchs (meter).
        speed (torch.tensor): Vector of shape (n), containing torch.float values of speeds (rotations/min).
        thrust (torch.tensor): Vector of shape (n), containing torch.float values of thrusts (neuton).
    """
    def __init__(self, n_propellers: int, propeller_diameters: list, propeller_pitchs: list):
        """
        Initilizes a class of n propellers.

        Attributes:
            n_propellers (int): Number of propellers, operating in one class.

            propeller_diameters (list): Vector of shape (n_propellers), containing torch.float values of diameters (meter).

            propeller_pitch (list): Vector of shape (n_propellers), containing torch.float values of pitchs (meter).
        """
        self.n = n_propellers
        if len(propeller_diameters) != n_propellers:
            raise ValueError(f"Shape of propeller_diameters ({len(propeller_diameters)}) not equal to n_propellers ({n_propellers}).")
        self.dia = torch.tensor(propeller_diameters) * 39.37 # to inches
        if len(propeller_pitchs) != n_propellers:
            raise ValueError(f"Shape of propeller_pitchs ({len(propeller_pitchs)}) not equal to n_propellers ({n_propellers}).")
        self.pitch = torch.tensor(propeller_pitchs) * 39.37 # to inches
        self.speed = torch.zeros((self.n))
        self.thrust = torch.zeros((self.n))
    


    def set_speed(self, propeller_speeds: torch.tensor):
        """
        Sets a speeds for propellers in class. Automaticly counts a trust for every propeller, according on speed.

        Attributes:
            speed (torch.tensor): Vector of shape (n), containing speed torch.float values for propellers (rotations/min).
        """
        if propeller_speeds.size(dim=0) != self.n:
            raise ValueError(f"Shape of speed ({propeller_speeds.shape}) not equal to n_propellers ({self.n}).")
        self.speed = propeller_speeds
        self.thrust = 4.392e-8 * self.speed * torch.pow(self.dia, 3.5) / (torch.sqrt(self.pitch))
        self.thrust =  self.thrust * (4.23e-4 * self.speed * self.pitch)
    
    # TODO: Add a forward alias for set_speed


# example of work:
# prop = Propellers(4, [3, 3, 3, 3], [2, 2, 2, 2])
# prop.set_speed(torch.tensor([3, 2, 1]))
