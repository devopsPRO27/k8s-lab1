# LAB1 test your knowalge !

## Pods

1. **What is the default pod status?**

2. **Which object defines a pod template?**

3. **What is the smallest deployable unit in Kubernetes?**

4. **What command lists all pods?**

5. **What is the command to delete a pod?**

---

## Deployments

1. **What is the purpose of a Deployment?**

2. **What command scales a deployment?**

3. **What object manages rolling updates?**

4. **What is used to define the desired state of a deployment?**

5. **What command updates a deployment?**

6. **What does a Deployment manage in Kubernetes?**

7. **What is the default number of replicas in a Deployment?**

---

## ReplicaSets

1. **What object ensures a specified number of pod replicas?**

2. **What does a ReplicaSet do?**

3. **What command lists ReplicaSets?**

4. **Which object is managed by a Deployment?**

5. **What ensures the availability of Pods in Kubernetes?**

6. **What happens if a pod managed by a ReplicaSet fails?**

---

## Service Types

1. **What service type exposes a pod internally in the cluster?**

2. **Which service type exposes the app to external traffic?**

3. **What type of service exposes a pod on a specific port?**

4. **Which service type is most commonly used for local development?**

5. **What command exposes a pod via a service?**

6. **What is the default service type?**

---

# answers

- **Answer**: `Running`
- **Answer**: `Deployment`
- **Answer**: `Pod`
- **Answer**: `kubectl get pods`
- **Answer**: `kubectl delete pod`
- **Answer**: `Manage replicas`
- **Answer**: `kubectl scale`
- **Answer**: `Deployment`
- **Answer**: `Spec`
- **Answer**: `kubectl apply`
- **Answer**: `Pods`
- **Answer**: `1`
- **Answer**: `ReplicaSet`
- **Answer**: `Maintain replicas`
- **Answer**: `kubectl get replicasets`
- **Answer**: `ReplicaSet`
- **Answer**: `ReplicaSet`
- **Answer**: `Recreated`
- **Answer**: `ClusterIP`
- **Answer**: `LoadBalancer`
- **Answer**: `NodePort`
- **Answer**: `NodePort`
- **Answer**: `kubectl expose`
- **Answer**: `ClusterIP`
