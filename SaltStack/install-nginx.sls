nginx:
  pkg:
    - installed
  service:
	- running
    - reload: true
	- enable: true    
