**Authors-Paradise(API)**

**Description**

Authors' Paradise is a full-fledged blog platform inspired by Medium,   offering a robust suite of features for writers and readers alike.   Here's what you can expect:

**Seamless User Experience:**   Create an account, securely manage your profile, and explore a world of engaging content.
**Content Creation Powerhouse:**   Craft compelling blog posts, effortlessly edit existing ones, and purge outdated entries with ease.
**Engaging Interactions:**   Foster a vibrant community through likes, comments, and bookmarking capabilities.  

**Key Technologies**  
+ **Backend:** Django (framework),Postgres(Database), Celery (task queue), Redis (in-memory data store),Nginix(Reverse Proxy Manager)
+ **Deployment:** Docker (containerization),Portainer(Docker Container manager),  AWS EC2 (cloud hosting)  

**Features:**   
+ **User Authentication:**   Secure login and registration with token-based authentication.
+ **Blog Management:**   Add, edit, and delete blog posts with user-friendly interfaces.
+ **Social Interactions:**   Like, comment on, and bookmark posts to promote engagement.
+ **Real-Time Experience:**   Flower (Celery monitoring tool) ensures smooth background tasks like comment notifications and blog rating updates, leading to a dynamic user experience.
+ **Scalability and Performance:**   Nginx (webserver), Celery, and Redis provide a robust foundation for handling high traffic volumes efficiently.


**Getting Started (Local Development):**  
- **Prerequisites**    
  - Python3  
  - Postgresql  
  - Docker    
  - Docker Compose      

- **Clone the repository:** 
 
  git clone https://github.com/towhid7667/authors-paradise-api/tree/main  
  cd authors-paradise   

- **Start the Docker containers:**  
sudo make build   
Access the API documentation at **http://localhost:8080/redoc**.  

**Live API Documentation:**  
- **https://authors-api.duckdns.org/redoc**

**Contact**  
For any inquiries or feedback, please contact **towhidulhq@gmail.com**.   
