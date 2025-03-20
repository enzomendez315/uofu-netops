package com.enzomendez.uofu_netops.ssh;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/ssh")
public class SshController {
    private final SshService sshService;

    public SshController(SshService sshService) {
        this.sshService = sshService;
    }

    @GetMapping("/connect")
    public String connectToSwitch(@RequestParam String host,
                                  @RequestParam String username,
                                  @RequestParam String password,
                                  @RequestParam(defaultValue = "show ip interface brief") String command) {
        return sshService.executeCommand(host, username, password, command);
    }
}
