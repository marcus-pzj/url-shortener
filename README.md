# url-shortener
URL shortener project conducted for "Building a Real-World Scalable Service" Workshop by Shopee

Run:  
```docker-compose build```  
```docker-compose up -d```  
```./db/create-schema.sh```  
```./acceptance-test/run.sh```  

Check that all tests passed.

Permission errors when running shell scripts:  
```find . -type f -iname "*.sh" -exec chmod +x {} \;```
