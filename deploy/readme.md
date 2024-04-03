## Curriculum Deploy (2024-03-28)

### Prep Work

1. Download latest draft release in [Github](https://github.com/Hello-World-CS/curriculum/releases/tag/v24.03.28) - v24.03.28
    
    * Moved the downloaded folder `v24.03.28` to `curriculum/deploys/`

2. Run this [workflow](https://github.com/Hello-World-CS/curriculum/actions/workflows/deploy-changes.yaml) - right now it is only printing the cmds that we need to execute to update only what changed.

    * I ran it manually in my computer

#### Delta Tags

| Version  | Tag       |
| -------- |-----------|
| Current  | v24.03.28 |
| Previous | v24.03.21 |

#### Courses w/Changes

1. Results comparing folders `diffs/local` with `diffs/prod`

- [ ] data-science-and-ai-a                                        COURSE=data-science-and-ai-a 
Nothing to do. Added/Updated texts and some blocks to project's block groups.
----

- [ ] java-fundamentals                                            COURSE=java-fundamentals 
Nothing to do. Added/Updated texts and some blocks to project's block groups.
----

- [ ] virtual-reality-c                                            COURSE=virtual-reality-c 
  * [ ] course.json
  * [ ] passion-project-team-level-4                                 a6c8b6b9-2760-41dc-b4af-7b0e1a848970
Nothing to do. Added new projects to course. Updated some project's texts. Added and renamed some assets.
----

- [ ] virtual-reality-c-practice-problems                          COURSE=virtual-reality-c-practice-problems 
  * [ ] course.json
  * [ ] level-3-independent-projects-practice-problem-1              92e389df-2c61-481c-883b-e0a6825f78eb
  * [ ] level-3-independent-projects-practice-problem-10             12e078ee-96d1-419e-b8e4-c6d9302aaf2a
  * [ ] level-3-independent-projects-practice-problem-11             95cd188b-7654-410e-935c-f43cdb12aa19
  * [ ] level-3-independent-projects-practice-problem-12             ef0af9b8-aedb-4a87-8db7-1cf9c406940c
  * [ ] level-3-independent-projects-practice-problem-13             df41f59e-4ea7-498f-8d57-d6b3626974db
  * [ ] level-3-independent-projects-practice-problem-14             687c7615-febb-45b7-aab9-48c77bf5de03
  * [ ] level-3-independent-projects-practice-problem-15             2bb3a4f3-f2c5-4e60-82b1-25e0b3e5998c
  * [ ] level-3-independent-projects-practice-problem-16             2626e0b1-670c-4a6c-b78f-4cbe1bb02de1
  * [ ] level-3-independent-projects-practice-problem-17             e468b56c-e3f1-4ab8-8754-105383cee032
  * [ ] level-3-independent-projects-practice-problem-18             4cd93e65-870e-4dbb-8c12-bc8e44fec98c
  * [ ] level-3-independent-projects-practice-problem-19             56c22a5c-9dfc-4471-a859-f93d932228bc
  * [ ] level-3-independent-projects-practice-problem-2              2b528cf3-632c-431c-bb12-1d80a1619787
  * [ ] level-3-independent-projects-practice-problem-20             57d16a37-7eb3-46fd-ae3d-88385c5d87e4
  * [ ] level-3-independent-projects-practice-problem-21             a9a61f9a-c5c3-4c7d-bd75-c70f6ecec59e
  * [ ] level-3-independent-projects-practice-problem-22             04594434-94c8-4cfc-81c7-a04546c67994
  * [ ] level-3-independent-projects-practice-problem-23             1c277ab1-2a21-42b6-9c9f-44e85b4316ee
  * [ ] level-3-independent-projects-practice-problem-24             1a8ac8db-33b8-46a2-9a86-fce83d6c4734
  * [ ] level-3-independent-projects-practice-problem-3              976eb0bd-9e82-428a-b720-faef7259de06
  * [ ] level-3-independent-projects-practice-problem-4              bda6eb8e-936f-4358-8526-946e2b00be2e
  * [ ] level-3-independent-projects-practice-problem-5              7ae938fe-c324-4d0a-80ba-fa39c33f5911
  * [ ] level-3-independent-projects-practice-problem-6              f3e2bb57-b2e0-47c5-b3d0-2c08b5e5f521
  * [ ] level-3-independent-projects-practice-problem-7              b28c3df6-2250-465f-a389-b6e80224a5ac
  * [ ] level-3-independent-projects-practice-problem-8              56fc76a4-6c2e-493d-b20f-36bd9bd430b2
  * [ ] level-3-independent-projects-practice-problem-9              35d4bb5a-f045-43a6-945e-9a377322303c
Nothing to do. Added new projects to course. Updated some project's texts. Added and renamed some assets.
----

- [ ] virtual-reality-d                                            COURSE=virtual-reality-d 
Nothing to do. Removed assets without updates to json's files.
----

2. Commands to be executed. List was created by this workflow [execution](https://github.com/Hello-World-CS/curriculum/actions/runs/8172797116/job/22343816732), `Deploy Course` step. It used `git-diff-changes.md` to prepare the list

*DEMO*
```
   sh tools/deploy/deploy-course-to-environment.sh --course data-science-and-ai-a --environment demo --allow-demo --project detective

   sh tools/deploy/deploy-course-to-environment.sh --course java-fundamentals --environment demo --allow-demo --project disco-dancer --project temporary-tattoo

   sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-c-practice-problems --environment demo --allow-demo --project clubhouse-practice-problem-8 --project level-3-independent-projects-practice-problem-1 --project level-3-independent-projects-practice-problem-10 --project level-3-independent-projects-practice-problem-11 --project level-3-independent-projects-practice-problem-12 --project level-3-independent-projects-practice-problem-13 --project level-3-independent-projects-practice-problem-14 --project level-3-independent-projects-practice-problem-15 --project level-3-independent-projects-practice-problem-16 --project level-3-independent-projects-practice-problem-17 --project level-3-independent-projects-practice-problem-18 --project level-3-independent-projects-practice-problem-19 --project level-3-independent-projects-practice-problem-2 --project level-3-independent-projects-practice-problem-20 --project level-3-independent-projects-practice-problem-21 --project level-3-independent-projects-practice-problem-22 --project level-3-independent-projects-practice-problem-23 --project level-3-independent-projects-practice-problem-24 --project level-3-independent-projects-practice-problem-3 --project level-3-independent-projects-practice-problem-4 --project level-3-independent-projects-practice-problem-5 --project level-3-independent-projects-practice-problem-6 --project level-3-independent-projects-practice-problem-7 --project level-3-independent-projects-practice-problem-8 --project level-3-independent-projects-practice-problem-9

   sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-d-practice-problems --environment demo --allow-demo --project 2.4_independent-projects-practice-problem-14 --project 2.4_independent-projects-practice-problem-10 --project 2.4_independent-projects-practice-problem-12 --project 2.4_independent-projects-practice-problem-13 --project 2.4_independent-projects-practice-problem-9

   sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-c --environment demo --allow-demo --project passion-project-team-level-4
```

### Updating the release

1. In [Github](https://github.com/Hello-World-CS/curriculum/releases) the draft release used to get the diffs was published: `v24.03.28`. Steps were:
  * Click in the `pen` icon
  * Confirm:
    * tag is correctly set (equal to version name)
    * only `Set as the latest release` is checked
    * click `Publish`

### Demo Env Steps

#### STEP 1
* [x] Create backup of database https://console.cloud.google.com/sql/instances/demo/backups?project=helloworldcs-demo
* [x] Delete the oldest curriculum deploy backup

#### STEP 2
* [x] Delete project progress: https://api.demo.helloworldcs.org/console/data/sql
    DELETE FROM project_progress;

#### STEP 3
Deploy the courses using cmds above

* [x] data-science-and-ai-a
* [x] java-fundamentals
* [x] virtual-reality-c-practice-problems
* [x] virtual-reality-d-practice-problems
* [x] virtual-reality-c

### Prod Env Steps

#### STEP 1

* [x] Create backup of database https://console.cloud.google.com/sql/instances/prod-db/backups?project=helloworldcs-b85f2&supportedpurview=project
* [x] Delete the oldest curriculum deploy backup

#### STEP 2
*PROD*
```
   sh tools/deploy/deploy-course-to-environment.sh --course data-science-and-ai-a --environment prod --project detective --allow-prod

   sh tools/deploy/deploy-course-to-environment.sh --course java-fundamentals --environment prod --project disco-dancer --project temporary-tattoo --allow-prod

   sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-c-practice-problems --environment prod --project clubhouse-practice-problem-8 --project level-3-independent-projects-practice-problem-1 --project level-3-independent-projects-practice-problem-10 --project level-3-independent-projects-practice-problem-11 --project level-3-independent-projects-practice-problem-12 --project level-3-independent-projects-practice-problem-13 --project level-3-independent-projects-practice-problem-14 --project level-3-independent-projects-practice-problem-15 --project level-3-independent-projects-practice-problem-16 --project level-3-independent-projects-practice-problem-17 --project level-3-independent-projects-practice-problem-18 --project level-3-independent-projects-practice-problem-19 --project level-3-independent-projects-practice-problem-2 --project level-3-independent-projects-practice-problem-20 --project level-3-independent-projects-practice-problem-21 --project level-3-independent-projects-practice-problem-22 --project level-3-independent-projects-practice-problem-23 --project level-3-independent-projects-practice-problem-24 --project level-3-independent-projects-practice-problem-3 --project level-3-independent-projects-practice-problem-4 --project level-3-independent-projects-practice-problem-5 --project level-3-independent-projects-practice-problem-6 --project level-3-independent-projects-practice-problem-7 --project level-3-independent-projects-practice-problem-8 --project level-3-independent-projects-practice-problem-9 --allow-prod

   sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-d-practice-problems --environment prod --project 2.4_independent-projects-practice-problem-14 --project 2.4_independent-projects-practice-problem-10 --project 2.4_independent-projects-practice-problem-12 --project 2.4_independent-projects-practice-problem-13 --project 2.4_independent-projects-practice-problem-9 --allow-prod

   sh tools/deploy/deploy-course-to-environment.sh --course virtual-reality-c --environment prod --project passion-project-team-level-4 --allow-prod
```

*Deploy the courses with no migrations*

* [x] data-science-and-ai-a
* [x] java-fundamentals
* [x] virtual-reality-c-practice-problems
* [x] virtual-reality-d-practice-problems
* [x] virtual-reality-c

### Notifying the team

1. In `#mission-control` Slack channel, this message was sent:

Hello @here! A curriculum deploy to prod and demo environments has been completed. Notes about the curriculum changes in the deployment can be found here and below is the full list of deployed courses based in the changes we found.
* data-science-and-ai-a
* java-fundamentals
* virtual-reality-c-practice-problems
* virtual-reality-d-practice-problems
* virtual-reality-c
