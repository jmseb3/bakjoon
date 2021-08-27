n = int(input())
node_data = {}
for _ in range(n):
    p_node, left_node, right_node = map(str, input().split())
    node_data[p_node] = [left_node, right_node]

def front(start_node):
    print(start_node, end="")
    left_node = node_data[start_node][0]
    right_node = node_data[start_node][1]
    if(left_node != '.'):
        front(left_node)
    if(right_node != '.'):
        front(right_node)

def mid(start_node):
    left_node = node_data[start_node][0]
    right_node = node_data[start_node][1]
    if(left_node != '.'):
        mid(left_node)
    print(start_node,end="")
    if(right_node != '.'):
        mid(right_node)

def end(start_node):
    left_node = node_data[start_node][0]
    right_node = node_data[start_node][1]
    if(left_node != '.'):
        end(left_node)
    if(right_node != '.'):
        end(right_node)
    print(start_node,end="")


        
front('A')
print()
mid('A')
print()
end('A')