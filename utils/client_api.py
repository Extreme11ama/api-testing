import requests
import logging

BaseURL = "https://jsonplaceholder.typicode.com"
logging.basicConfig(level=logging.INFO)

class APIClient:
    def getPost(self, postID):
        logging.info(f"Getting post {postID}")
        return requests.get(f"{BaseURL}/posts/{postID}")
    
    def getAllPosts(self):
        logging.info(f"Getting all posts")
        return requests.get(f"{BaseURL}/posts")
    
    def createPost(self, body):
        logging.info(f"Creating new post")
        return requests.post(f"{BaseURL}/posts", json= body)
    
    def updatePost(self, postID, body):
        logging.info(f"Updating post {postID}")
        return requests.put(f"{BaseURL}/posts/{postID}", json=body)

    def deletePost(self, postID):
        logging.info(f"Deleting post {postID}")
        return requests.delete(f"{BaseURL}/posts/{postID}")