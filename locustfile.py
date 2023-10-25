import random
import time

from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [
                    {
                        "content": random.choice(
                            [
                                "What are best practices for preventing data leaks in my organization?",
                                "Does GitHub support two factor authentication?",
                                "What does a dependabot alert do?",
                                "What does verifying a domain for my organization do?",
                            ]
                        ),
                        "role": "user",
                    },
                ],
                "overrides": {
                    "retrieval_mode": "hybrid",
                    "semantic_ranker": True,
                    "semantic_captions": False,
                    "top": 3,
                    "suggest_followup_questions": False,
                },
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [
                    {"content": "What does a dependabot alert do?", "role": "user"},
                    {
                        "content": "Dependabot alerts tell you that your code depends on a package that is insecure. [About-Dependabot-alerts.pdf]. Dependabot performs a scan of the default branch of your repository to detect insecuredependencies [About-Dependabot-alerts.pdf]. GitHub detects vulnerable dependencies and malware in public repositories and displays thedependency graph, but does not generate Dependabot alerts by default. Repository owners orpeople with admin access can enable Dependabot alerts for public repositories. [About-Dependabot-alerts.pdf].",
                        "role": "assistant",
                    },
                    {"content": "What does verifying a domain for my organization do?", "role": "user"},
                ],
                "overrides": {
                    "retrieval_mode": "hybrid",
                    "semantic_ranker": True,
                    "semantic_captions": False,
                    "top": 3,
                    "suggest_followup_questions": False,
                },
            },
        )
