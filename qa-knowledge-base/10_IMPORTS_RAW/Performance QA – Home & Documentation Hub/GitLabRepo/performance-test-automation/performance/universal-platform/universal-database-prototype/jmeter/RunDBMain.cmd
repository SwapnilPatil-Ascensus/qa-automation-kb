@ECHO off
REM Set the path to the JMeter home directory
REM kubectl delete configmap ags-performance-testing -n ags-qa
REM kubectl delete jobs taurus -n ags-qa
kubectl delete configmap ags-performance-testing-db -n ags-qa
kubectl delete pod -n ags-qa perf-taurus-docker-pod-db
timeout 10

kubectl create configmap ags-performance-testing-db --namespace ags-qa --from-file TestRunDB.yml --from-file db_flow_main.jmx --from-file member_login.csv
timeout 10
kubectl apply -f perf-taurus-db.yaml -n ags-qa 
timeout 10
REM kubectl apply -f perf-taurus-csr.yaml -n ags-qa
REM kubectl apply -f perf-taurus-user.yaml -n ags-qa
REM helm uninstall ags-performance-testing -n ags-qa
REM helm install ags-performance-testing ./helm --namespace ags-qa --wait
timeout 10
REM kubectl logs -f --namespace=ags-qa jobs/taurus
REM kubectl logs -f -ljob-name=taurus -n ags-qa --all-containers=true
kubectl describe pod -n ags-qa perf-taurus-docker-pod-db
kubectl logs perf-taurus-docker-pod-db -n ags-qa