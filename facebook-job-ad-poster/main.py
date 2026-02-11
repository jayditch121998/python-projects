from app.services.job_ad_service import FacebookJobAdService

def main():
    service = FacebookJobAdService()

    job_data = [
        {
            "job_title": "Customer Support Representative",
            "job_level": "junior",
            "employment_type": "full-time",
            "work_arrangement": "onsite",
            "location": "Staffhouse Road, Baguio City Economic Zone PEZA, Loakan Road",
            "recipient_details": "careers@nms.ph",
            "description": (
                "Handle customer inquiries through email and chat. "
                "Assist customers with basic concerns, provide accurate information, "
                "and escalate complex issues to the appropriate team. "
                "Maintain a professional and helpful tone while ensuring timely responses."
            ),
            "salary": {
                "min": 18000,
                "max": 22000,
                "currency": "PHP",
                "period": "monthly"
            },
            "pay_schedule": "bi-monthly",
            "skills": [
                "Customer Communication",
                "Email Support",
                "Chat Support",
                "Basic Computer Skills"
            ]
        },
        {
            "job_title": "UI/UX Designer",
            "job_level": "mid",
            "employment_type": "full-time",
            "work_arrangement": "hybrid",
            "location": "Staffhouse Road, Baguio City Economic Zone PEZA, Loakan Road",
            "recipient_details": "careers@nms.ph",
            "description": (
                "Design intuitive user interfaces for web and mobile applications. "
                "Collaborate with product managers and developers to translate requirements "
                "into wireframes and prototypes. Ensure designs follow usability best "
                "practices and align with brand standards."
            ),
            "salary": {
                "min": 40000,
                "max": 65000,
                "currency": "PHP",
                "period": "monthly"
            },
            "pay_schedule": "bi-monthly",
            "skills": [
                "Figma",
                "Wireframing",
                "Prototyping",
                "User Research",
                "Design Systems"
            ]
        }
    ]

    result = service.create_and_post(
        page_id="631600456692933",
        job_data=job_data
    )

    print(result["ad_text"])

if __name__ == "__main__":
    main()
