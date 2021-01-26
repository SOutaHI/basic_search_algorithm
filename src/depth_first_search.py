
class DepthFirstSearch:

    def __init__(self, graph):

        print("depth first search start")
        
        self.graph            = graph
        self.state            = []
        self.open_list        = []
        self.closed_list      = []
        self.exploration_path = []
    

    def exploration(self):

        open_list   = []
        closed_list = []
        ret_value   = True
        graph       = self.graph
        goal_element = 2
        
        closed_list.append(4)

        temp_stack = []
        connection_node = graph[closed_list[-1]]
        graph[4] = None
        
        for i in connection_node:
            temp_stack.append(i)

        for i in open_list:
            temp_stack.append(i)
       
        open_list = temp_stack
           
        first_element = open_list[0]

        print("open list : ", open_list)
        print("closed list :", closed_list)
        print("\n")
      
        while len(open_list) != 0:

            if first_element == goal_element:
                closed_list.append(first_element)

                temp_stack = []
                connection_node = graph[closed_list[-1]]

                for i in connection_node:
                    temp_stack.append(i)

                for i in range(len(open_list) - 1):
                    temp_stack.append(open_list[i+1])

                open_list = temp_stack
                
                break

            else:
                closed_list.append(first_element)

            temp_stack = []
            
            if graph[closed_list[-1]] != None:
                connection_node        = graph[closed_list[-1]]                    
                graph[closed_list[-1]] = None
                
                for i in connection_node:
                    temp_stack.append(i)

            for i in range(len(open_list) - 1):
                temp_stack.append(open_list[i+1])
            
            open_list = temp_stack
           
            first_element = open_list[0]

            print("open list : ", open_list)
            print("closed list :", closed_list)           
            print("\n")
      

        print(open_list)
        self.closed_list = closed_list

        return ret_value

    def get_closed_list(self):

        closed_list = self.closed_list

        return closed_list

if __name__ == '__main__':
    pass