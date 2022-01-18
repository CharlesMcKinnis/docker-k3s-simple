docker buildx build -t revantine/deploy-docker-container --platform linux/arm/v7,linux/arm64/v8,linux/amd64 --push .

kubectl apply -f deployment.yaml
kubectl get ingress,svc,pods

kubectl delete service flask-test-service
kubectl delete deployment flask-test-app

