import requests

BaseURL = "https://jsonplaceholder.typicode.com"

class APIClient:
    def getPost(self, postID):
        return requests.get(f"{BaseURL}/posts/{postID}")
    
    def getAllPosts(self):
        return requests.get(f"{BaseURL}/posts")
    
    def createPost(self, body):
        return requests.post(f"{BaseURL}/posts", json= body)