@ECHO off
REM Set the path to the JMeter home directory
kubectl delete configmap ags-performance-testing-csr -n ags-qa
kubectl delete configmap ags-performance-testing-broker -n ags-qa
kubectl delete configmap ags-performance-testing-user -n ags-qa

REM kubectl delete jobs taurus -n ags-qa
kubectl delete pod -n ags-qa perf-taurus-docker-pod-csr
kubectl delete pod -n ags-qa perf-taurus-docker-pod-broker
kubectl delete pod -n ags-qa perf-taurus-docker-pod-user-2
kubectl delete pod -n ags-qa perf-taurus-docker-pod-user-3
kubectl delete pod -n ags-qa perf-taurus-docker-pod-user-1

REM kubectl delete pod -n ags-qa perf-taurus-docker-pod
REM kubectl create configmap ags-performance-testing --namespace ags-qa --from-file TestRun_CSRSearch.yaml --from-file csr_search.jmx
REM helm uninstall ags-performance-testing -n ags-qa
REM helm install ags-performance-testing ./helm --namespace ags-qa --wait
timeout 15
REM kubectl logs -f --namespace=ags-qa jobs/taurus
kubectl describe ns ags-qa
kubectl logs -f -ljob-name=taurus -n ags-qa --all-containers=true