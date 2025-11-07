# OpenPetCare: Veterinary Vaccine Schedule Dataset

Welcome to **OpenPetCare**! 🐾

This repository contains an open, easy-to-use dataset of **veterinary vaccine schedules for dogs and cats**. Our goal is to help pet owners, hobby developers, and pet enthusiasts understand preventive care timelines — in a structured, trustworthy, and human-readable format.  

> **Important:** This dataset is **for educational purposes only**. Always consult your veterinarian for advice specific to your pet.

---

## What’s Inside

The dataset includes:

- **Vaccine schedules** for dogs and cats, separated into **initial vaccinations** and **revaccinations/boosters**.  
- Information about **how vaccines are administered**, recommended ages, booster intervals, and what diseases each vaccine protects against.  
- Human-readable explanations of schedules to make the data approachable.  
- Source references so you know where the information comes from.

All the data is stored in CSV files and is easy to use in spreadsheets, apps, or scripts.

---

## Dataset Columns

| Column | What it Means | Example |
|--------|---------------|---------|
| `species` | Animal type | dog |
| `vaccine_name` | Name of vaccine | Bordatella |
| `category` | Core or non-core vaccine | core |
| `vaccination_stage` | Initial or revaccination | initial |
| `administration_route` | How the vaccine is given | intranasal |
| `age_min_weeks` | Minimum recommended age | 6 |
| `age_max_weeks` | Maximum recommended age | 16 |
| `booster_interval_min_weeks` | Minimum interval until first booster | 2 |
| `booster_interval_max_weeks` | Maximum interval until first booster | 4 |
| `booster_interval_years` | Years between boosters after the initial series | 3 |
| `recommended_frequency` | Human-readable summary of schedule | 2 doses, 2–4 weeks apart |
| `disease_targeted` | Disease the vaccine protects against | Bordatella bronchiseptica |
| `source` | Guideline or document the info came from | AAHA 2022 Canine Vaccination Guidelines |

---

## How to Use

- You can **filter by species, age, or vaccination stage** to plan preventive care timelines.  
- Track **dose intervals and boosters** using the numeric columns.  
- Reference the `source` column for credibility and further reading.  
- Feel free to use this dataset to **build apps, dashboards, or visualizations** for pet care.

---

## Contributing

We welcome contributions! Here’s how you can help:

1. Fork the repository.  
2. Add or update data in the CSV files.  
3. Update or add your sources in the `source` column.  
4. Submit a pull request describing your changes.  

**Tips:**  

- Double-check recommended ages and intervals.
- Keep human-readable notes clear and concise.  
- Use reputable sources like AAHA, WSAVA, or other recognized veterinary guidelines.

---

## License

This dataset is released under **Creative Commons Attribution 4.0 (CC BY 4.0)**. You are free to **use, share, and adapt** it as long as you provide credit.

---

## Disclaimer

This dataset is **not veterinary advice**. It is intended for informational and educational purposes only. Always consult a licensed veterinarian for medical guidance for your pets.
