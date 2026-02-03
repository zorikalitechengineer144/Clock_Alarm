import os
import random
from datetime import datetime, timedelta

# Define years: Full years (2020–2025) and partial 2026 (Jan only)
years = [2020, 2021, 2022, 2023, 2024, 2025, 2026]

# Commit count ranges
commit_ranges = {year: (400, 440) for year in years[:-1]}
commit_ranges[2026] = (20, 20)  # Exactly 20 commits in Jan 2026

# Commit options & probabilities
commit_options = [0, 1, 2, 3]
commit_weights = [0.05, 0.15, 0.5, 0.3]

def generate_commits(year, start_date, end_date, target_commits):
    total_commits = 0
    dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
    random.shuffle(dates)

    commit_distribution = {date: 0 for date in dates}

    # Distribute commits
    while total_commits < target_commits:
        for commit_date in dates:
            if total_commits >= target_commits:
                break
            commit_count = random.choices(commit_options, weights=commit_weights)[0]
            commit_count = min(commit_count, target_commits - total_commits)
            commit_distribution[commit_date] += commit_count
            total_commits += commit_count

    # Apply commits
    for commit_date, commit_count in commit_distribution.items():
        for _ in range(commit_count):
            # Randomize commit time for realism
            commit_date = commit_date.replace(
                hour=random.randint(0, 23),
                minute=random.randint(0, 59),
                second=random.randint(0, 59)
            )

            # Append to test file
            with open('test.txt', 'a') as file:
                file.write(f'Commit on {commit_date.strftime("%Y-%m-%d %H:%M:%S")}\n')

            os.system('git add test.txt')

            formatted_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
            os.environ["GIT_COMMITTER_DATE"] = formatted_date
            os.environ["GIT_AUTHOR_DATE"] = formatted_date
            commit_message = f"Automated commit on {commit_date.strftime('%Y-%m-%d')}"
            os.system(f'git commit --date="{formatted_date}" -m "{commit_message}"')

            print(f'✔ Committed on {commit_date.strftime("%Y-%m-%d %H:%M:%S")}')

    # Push once per year
    os.system('git push origin main')
    print(f'📤 All commits for {year} pushed!')

for year in years:
    print(f"\n🚀 Processing year {year}...")

    # Set start and end dates (simplified)
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31) if year < 2026 else datetime(year, 1, 31)

    target_commits = random.randint(*commit_ranges[year])

    generate_commits(year, start_date, end_date, target_commits)

print("\n🎉 All commits for all years have been successfully committed AND pushed (once per year)!")
