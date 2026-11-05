@ECHO off
REM Set the path to the JMeter home directory
REM kubectl delete configmap ags-performance-testing -n ags-qa
REM kubectl delete jobs taurus -n ags-qa
kubectl create configmap ags-performance-testing-broker --namespace ags-qa --from-file TestRunBroker.yml --from-file broker.jmx --from-file broker.csv
timeout 10
kubectl apply -f perf-taurus-broker.yaml -n ags-qa

REM helm uninstall ags-performance-testing -n ags-qa
REM helm install ags-performance-testing ./helm --namespace ags-qa --wait
timeout 10
REM kubectl logs -f --namespace=ags-qa jobs/taurus
REM kubectl logs -f -ljob-name=taurus -n ags-qa --all-containers=true
kubectl describe pod -n ags-qa perf-taurus-docker-pod-broker
kubectl logs perf-taurus-docker-pod-broker -n ags-qa