class UserCPFController(object):
    @staticmethod
    def validatingCpf(cpf):
        cpf = list([int(n) for n in cpf if n.isdigit()])

        return {
            "cpf": formatCpf(cpf),
            "isValid": validateCpf(cpf)
        }

    @staticmethod
    def getGeneratedCpf(User, num_list_cpf):
        if User.count() > 0:
            cpfs = User.first().my_cpfs
            my_cfs = []
            for cpf in cpfs:
                my_cfs.append(cpf.cpf)

            def findValidCpfGenerated():
                cpf = generateRandomCpf()
                while not validateCpf(cpf) or formatCpf(cpf) in my_cfs:
                    cpf = generateRandomCpf()

                return cpf

            my_list_cpf = []

            for num in range(num_list_cpf):
                my_list_cpf.append(formatCpf(findValidCpfGenerated()))

            return {
                "my_list_cpf": my_list_cpf
            }
        else:
            return {
                "message": {
                    "error": "username sent don't found"
                }
            }


def generateRandomCpf():
    import random
    cpf = []

    for i in range(11):
        n = random.randint(0, 9)
        cpf.append(n)
    return cpf


def formatCpf(format_cpf):
    cpf = ""
    for n in format_cpf:
        cpf += str(n)
    return "%s.%s.%s-%s" %(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:])


def concatingDivision1(i, n):
    return (i + 2) * n


def concatingDivision2(i, n):
    return (i + 3) * n


def resolvingDivision1(division1):
    return ((division1 * 10) % 11) % 10


def resolvingDivision2(division1, division2):
    return (((division2 + division1 * 2) * 10) % 11) % 10


def getDivision(cpf):
    division1 = division2 = 0
    last_digits = ""

    for i, n in enumerate(cpf):
        if i < 9:
            division1 += concatingDivision1(i, n)
            division2 += concatingDivision2(i, n)
        else:
            last_digits += str(n)
    division1 = resolvingDivision1(division1)
    return [str(resolvingDivision2(division1, division2)) + str(division1), last_digits]


def validateCpf(cpf):
    division = getDivision(cpf)
    return bool(division[0] == division[1])
