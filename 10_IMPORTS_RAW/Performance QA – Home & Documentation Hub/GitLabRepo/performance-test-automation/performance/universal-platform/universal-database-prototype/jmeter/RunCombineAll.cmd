@ECHO off
REM Set the path to the JMeter home directory
kubectl delete configmap ags-performance-testing-user -n ags-qa
kubectl delete configmap ags-performance-testing-csr -n ags-qa
kubectl delete configmap ags-performance-testing-broker -n ags-qa
kubectl delete deployments perf-taurus-deployment-user -n ags-qa
timeout 10
REM kubectl delete jobs taurus -n ags-qa
kubectl create configmap ags-performance-testing-csr --namespace ags-qa --from-file TestRunCSR.yml --from-file csr_search.jmx --from-file csr_acct_search.csv --from-file csr_login.csv
kubectl create configmap ags-performance-testing-user --namespace ags-qa --from-file TestRunUser.yml --from-file userProfile.jmx --from-file tf_member_login.jmx --from-file tf_member_logout.jmx --from-file tf_account_overview.jmx --from-file member_login.csv
kubectl create configmap ags-performance-testing-broker --namespace ags-qa --from-file TestRunBroker.yml --from-file broker.jmx --from-file broker.csv

timeout 10
kubectl apply -f perf-taurus-combine.yaml -n ags-qa

timeout 10
kubectl describe pod -n ags-qa
kubectl get pod -n ags-qa