npm i
npm run build
docker build --no-cache -t dineshsonachalam/tech-courses-search-engine-frontend:latest .
docker push dineshsonachalam/tech-courses-search-engine-frontend:latest