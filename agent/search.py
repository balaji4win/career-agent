from pathlib import Path
import yaml

PROFILE = Path("profile/profile.yaml")


def load_profile():
    with PROFILE.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    profile = load_profile()

    print("Career Agent started")
    print("=" * 50)

    print("Target roles:")
    for role in profile["candidate"]["target_roles"]:
        print(f"  - {role}")

    print("\nDomains:")
    for domain in profile["candidate"]["domains"]:
        print(f"  - {domain}")

    print("\nTechnical skills:")
    for skill in profile["candidate"]["technical"]:
        print(f"  - {skill}")


if __name__ == "__main__":
    main()
