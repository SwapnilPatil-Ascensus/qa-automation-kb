@ECHO off
REM Set the path to the JMeter home directory
REM kubectl delete configmap ags-performance-testing -n ags-qa
REM kubectl delete jobs taurus -n ags-qa
kubectl create configmap ags-performance-testing-user --namespace ags-qa --from-file TestRunUser.yml --from-file userProfile.jmx --from-file tf_member_login.jmx --from-file tf_member_logout.jmx --from-file tf_account_overview.jmx --from-file member_login.csv

timeout 10
REM kubectl apply -f perf-taurus-csr.yaml -n ags-qa
kubectl apply -f perf-taurus-user.yaml -n ags-qa
REM helm uninstall ags-performance-testing -n ags-qa
REM helm install ags-performance-testing ./helm --namespace ags-qa --wait
timeout 10
REM kubectl logs -f --namespace=ags-qa jobs/taurus
REM kubectl logs -f -ljob-name=taurus -n ags-qa --all-containers=true
kubectl describe pod -n ags-qa perf-taurus-docker-pod-user
kubectl logs perf-taurus-docker-pod-user -n ags-qa