class Target:
    """The target defines interface used by the client code."""
    def request(self):
        return "Target: The default target's behavior." 
    
class Adaptee:
    """The Adaptee defines an existing interface that needs adapting."""
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target, Adaptee):
    def request(self):
        return f'Adapter: {self.specific_request()[::-1]}'


def client_code(target):
    """The client code supports all classes that follow the Target interface."""
    print(target.request())


if __name__ == "__main__":
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    adapter = Adapter()

    client_code(adapter)
