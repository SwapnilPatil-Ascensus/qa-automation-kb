@ECHO off
REM Set the path to the JMeter home directory
kubectl delete configmap ags-performance-testing-user-stage -n ags-qa
timeout 10
REM kubectl delete jobs taurus -n ags-qa
kubectl create configmap ags-performance-testing-user-stage --namespace ags-qa --from-file TestRunUserStage1.yml --from-file csr_acct0verview_stage1.jmx --from-file encryptedStage.csv --from-file secretKeyStage.txt --from-file csr_account_search_Prod.csv
REM kubectl delete deployments perf-taurus-deployment-user -n ags-qa
kubectl delete pod perf-pod-user-stage1 -n ags-qa
timeout 10
REM kubectl apply -f userProfileDeployment.yml -n ags-qa
REM kubectl apply -f perf-taurus-csr.yaml -n ags-qa
kubectl apply -f perf-taurus-user-stage1.yaml -n ags-qa

timeout 10
REM kubectl logs -f --namespace=ags-qa jobs/taurus

REM kubectl logs -f -ljob-name=taurus -n ags-qa --all-containers=true
REM kubectl describe pod -n ags-qa perf-taurus-deployment-user-6dc64b45cf-775cb
REM kubectl logs perf-taurus-docker-pod-user -n ags-qa
kubectl logs perf-pod-user-stage1 -n ags-qa
kubectl get pod -n ags-qa