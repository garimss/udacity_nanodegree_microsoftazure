# Write-up 

## Analyze, choose, and justify the appropriate resource option for deploying the app.

**Answer:** 
### Analyse

**Azure App Service** is described as “Build, deploy, and scale web apps on a fully managed platform and web apps can be created with popular frameworks such as .NET, .NET Core, Node.js, Java, PHP, Ruby, Or Python in containers or running on any operating system. Azure APP Service referred as “Platform as a Service (PaaS)” that allows a developer to focus on the application while Azure takes care of the infrastructure. Azure App Service is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends.

**Some of the benefits of using an App Service are:**

    - Support of multiple languages, such as .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python
    - High availability, auto-scaling and support of both Linux and Windows environments.
    - Continuous deployment model using GitHub, Azure DevOps, or any Git repo.
    - Vertical or Horizontal scaling. Vertical scaling increases or decreases resources allocated to our App Service, such as the amount of vCPUs or RAM, by changing the App Service pricing tier. Horizontal scaling increases or decreases the number of Virtual Machine instances our App Service is running.
    - You can set the amount of hardware allocated to host your application, and cost varies based on the plan you choose. There are three different tiers - Dev/Test, Production, and Isolated. 

**Some of the limitations of an App Service are:**

    - You have limited access to the host server, so you are unable to control the underlying OS or install software on the server.
    - You’re always paying for the service plan, even if your services or application isn’t running.
    - There are hardware limitations, such as a maximum of 14GB of memory and 4 vCPU cores per instance
    - While they support multiple languages, as noted in the benefits above, they are limited to just using those languages (as of when this course was built).

On the other hand **Virtual Machines** is described as "*It provides on-demand, high-scale, secure, virtualized infrastructure *". You can create Linux and Windows virtual machines. It gives you the flexibility of virtualization for a wide range of computing solutions—development and testing, running applications, and extending your datacenter. It is the freedom of open-source software configured the way you need it. Azure Virtual Machines (VMs) provide infrastructure as a service (IaaS) by allowing you to create and use virtual machines in the cloud.

**Some of the benefits of VMs are:**

    - VMs allow you full access and control of the VM.
    - Lower up-front cost compared to purchasing and maintaining hardware.
    - Support of both Linux and Windows VMs.
    - Multiple types to choose from, such as compute or memory-optimized VMs, along with varying amounts of CPU, RAM and storage.
    - VMs allow for the installation of custom images and are an excellent choice for migrating from an on-premises server to the cloud.
    - Multiple VMs can be grouped to provide high availability, scalability, and redundancy. There are two options when it comes to scaling—Virtual Machine Scale Sets and Load Balancers. These will be covered in a different course.

**Some of the limitations of VMs are:**

    - They are more expensive
    - They can be more time consuming for the developer than other compute options

### Choose

To create ArticleCMS web app , I will select **Azure App Service** as this serves the purpose of app.

### Justify

**I have selected Azure App Service for many reasons:**
- *since it is used to host web apps, it makes the best choice.* 
- *It can be used with python.*
- *It allows to set the amount of hardware allocated to host application, and cost varies based on the plan I choose. For experiment purpose I set F1 free tier, which is free for 1 GB*
- *auto-scalable*
- *High-Variability*
- *App Service is a PaaS offering meaning that you just have to deploy your code and not worry about the underlying infrastructure.*
- *The application is designed to be cloud native removing the need for server management and optimization.*
- *It also has good pricing tiers and gives adequate room for scalability.* 
- *wide range of deployment options are available that can easily be integrated into a production workflow*




*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

*Costs:* In terns of cost, an App service would be more flexible since more than one app can be made to share the App Service plan while a Virtual machine has the advantage of being able to be deallocated when not in use in order to cut costs.

*Scalability:* Both the Virtual machine and the App Service can be scalled horizontally and vertically. VMs can be scalled horizontally using a VMSS, while App Service's have native Auto scalling properties.

*Availability:* In terms of availability Virtual machines generally have more availability than App Services, but require extra setup and configuration to be fault tolerant and avoid downtimes during maintenance and upgrades.

*Workflow:* It is fairly easier to deploy applications to App Service than it is to Virtual Machines. Although an automated CI/CD pipeline could be designed to resolve this issue, overhead time would be spent in the process.




### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

*These are the points which can change the decision on last minute*
- *If the app requires control over server or operating system, I need to move to Virtual Machine.*
- *App Service's are limited 14 GB of Memory and 4 VCPUs. If the application were to be a high compute application the need to extend hardware requirements would call for a Virtual Machine.* 
- *A need to utilize custom monitoring and logging solutions could also necessitate a use VMs.* 
- *If our app should not run always, we should use Virtual Machine to save the cost. For this we will need to stop the virtual machine when not require to use. In App service we are totally depend on service plan, weather we use or no, we will need to pay.*
- *If App service does not offer the programming language of code which our app is written in.*

