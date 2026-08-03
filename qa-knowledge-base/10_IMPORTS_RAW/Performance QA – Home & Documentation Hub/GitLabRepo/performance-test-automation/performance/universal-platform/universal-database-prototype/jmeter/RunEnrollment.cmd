@ECHO off
REM Set the path to the JMeter home directory
kubectl delete configmap ags-performance-testing-enrollment -n ags-qa
timeout 10
REM kubectl delete jobs taurus -n ags-qa
kubectl create configmap ags-performance-testing-enrollment --namespace ags-qa --from-file TestRunEnrollment.yml --from-file ue_enrollment_D.jmx
REM kubectl delete deployments perf-taurus-deployment-user -n ags-qa
kubectl delete pod perf-taurus-pod-enrollment -n ags-qa


timeout 10
REM kubectl apply -f userProfileDeployment.yml -n ags-qa
REM kubectl apply -f perf-taurus-csr.yaml -n ags-qa
kubectl apply -f perf-taurus-enrollment.yaml -n ags-qa

timeout 10
REM kubectl logs -f --namespace=ags-qa jobs/taurus
REM kubectl logs -f -ljob-name=taurus -n ags-qa --all-containers=true
REM kubectl describe pod -n ags-qa perf-taurus-deployment-user-6dc64b45cf-775cb
REM kubectl logs perf-taurus-docker-pod-user -n ags-qa
kubectl logs perf-taurus-pod-enrollment -n ags-qa
kubectl get pod -n ags-qa