<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>

<body>

    <h1>User Registration Form</h1>

    <form action="/submit" method="post">
        
        <label for="fullname">Full Name:</label><br>
        <input type="text" id="fullname" name="fullname" required maxlength="100" placeholder="Enter your full name"><br><br>

        <label for="email">Email Address:</label><br>
        <input type="email" id="email" name="email" required placeholder="Enter your email address"><br><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required minlength="8" placeholder="Enter your password"><br><br>

        <label for="age">Age:</label><br>
        <input type="number" id="age" name="age" required min="18" placeholder="Enter your age"><br><br>

        <label>Gender:</label><br>
        <input type="radio" id="male" name="gender" value="Male" required>
        <label for="male">Male</label><br>
        <input type="radio" id="female" name="gender" value="Female" required>
        <label for="female">Female</label><br>
        <input type="radio" id="other" name="gender" value="Other" required>
        <label for="other">Other</label><br><br>

        <label for="terms">
            <input type="checkbox" id="terms" name="terms" required>
            I agree to the <a href="#">terms and conditions</a>.
        </label><br><br>

        <button type="submit">Register</button>

    </form>

</body>

</html>
