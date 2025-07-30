# The Impact of Cognitive Load on Physical Performance: A Wearable Sensor-Based Investigation

This repository contains the full implementation, data processing pipeline, and analysis code for our study: “The Impact of Cognitive Load on Physical Performance”. We investigate how performing a mental task (serial subtraction) affects physical activity using wearable IMU sensors across three daily activities: Sit-to-Stand, Drinking Water, and Step-Count.

### Tasks:
1. **Sit-to-Stand** – Repetition count in 30s  
2. **Drinking Water** – Completion time in seconds
3. **Step Count** – Steps taken in 30s  
<img width="1174" height="498" alt="3_tasks" src="https://github.com/user-attachments/assets/e7ab804f-6c45-4941-b849-68512cb58913" />

---

## Statistical Methods

- **Sensors**: Movella DOT IMUs (abdomen, wrist, ankle)  
- **Conditions**:  
  - *Standard*: Physical task only  
  - *Cognitive Load*: Task + backward counting by 7s  

### Feature Extraction:
- Acceleration magnitude & velocity
- Task-specific features (No. of Sit-to-Stand repetitions, Time taken for Drinking water task, No. of Steps)

### Analysis:
- **Stats**: Paired t-tests & Wilcoxon tests (α = 0.05)  
- **ML**:  
  - *Unsupervised*: K-Means on Sit-to-Stand to cluster standard vs cognitive data groups (80% accuracy)  
  - *Supervised*: Train several models to detect standard vs cognitive task conditions in Step count. Best model: Random Forest (85% accuracy)

---

## Key Results

| Task            | Metric Impacted          | Significant? |
|-----------------|--------------------------|--------------|
| Sit-to-Stand    | Fewer repetitions        | ✅ p = 0.01  |
| Drinking Water  | Longer completion time   | ✅ p = 0.001 |
| Step Count      | Fewer steps              | ✅ p = 0.002 |

---

## Project Structure
```
notebooks/        # Analysis per task
data/             # Raw IMU data
utils/            # Helper scripts to help organize and aggregate csv files
```
---

## How to Run Locally?

```bash
git clone https://github.com/ashishpatel16/ds4w-impact-of-cognitive-load-on-physical-performance.git
cd cognitive-load-performance
pip install -r requirements.txt
jupyter notebook notebooks/
```


---

### Contributors

Ashish Patel · Nour Farhat · Xhoel Bano
Chair of Digital Health – Hasso Plattner Institute
