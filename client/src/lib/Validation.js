export const isEmail = (email) => {
    {
        const regex = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/;
        return email.match(regex);
    }
}

export const isPassword = (password) => (password.length >= 6)