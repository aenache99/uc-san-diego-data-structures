class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Use a dictionary to store contacts with phone numbers as keys
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # Add or update the contact in the dictionary
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            # Remove the contact if it exists
            contacts.pop(cur_query.number, None)
        else:
            # Search for the contact by phone number
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
